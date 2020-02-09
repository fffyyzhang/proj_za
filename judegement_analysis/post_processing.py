import collections
import re
import copy


def labels_to_list(labels, name):
    sents = {}
    for label in labels:
        sents[label[0]] = {'文档名称': name, '判决语句编号': label[0], 'order': []}
    for i, label in enumerate(labels):
        k = re.match(r'[a-zA-Z-]+', label[1]).group()

        # 原告在句首时很容易被误分为payer(反诉为特例)，这里做临时修正
        if i == 0 and k == 'payer' and '原告' in label[2]:
            k = 'payee'
            print("Tmp fix for labeling:{}".format(label[2]))

        if k not in sents[label[0]]:
            sents[label[0]][k] = []
        sents[label[0]][k].append(label[2])
        sents[label[0]]['order'].append(k)
    return sents


def compensation_extraction(_sent):
    sent = copy.deepcopy(_sent)
    res = []

    base = {
        'n_doc_id': sent['文档名称'],
        'judgmentItemNo': sent['判决语句编号']
    }
    win = {
        **base,
        'role': '被给付方',
    }
    if 'payee' in sent:
        # 被给付人名称不全为原告
        payee_has_name = False
        for name in sent['payee']:
            if name != '原告':
                payee_has_name = True
        payee = list(set([x for x in sent['payee'] if x != '原告' or not payee_has_name]))
        payee.sort(key=sent['payee'].index)

        if len(payee) == 1:
            win['organization/person name'] = payee[0]
        elif len(payee) > 1:
            win['organization/person name'] = '、'.join(payee)

    lose = {
        **base,
        'role': '给付方'
    }
    if 'payer' in sent:
        # 给付人名称不全为被告
        payer_has_name = False
        for name in sent['payer']:
            if name != '被告':
                payer_has_name = True
        payer = list(set([x for x in sent['payer'] if x != '被告' or not payer_has_name]))
        payer.sort(key=sent['payer'].index)
        if len(payer) == 1:
            lose['organization/person name'] = payer[0]

            label_count = collections.Counter()
            for i in range(len(sent['order']) - 1):
                if sent['order'][i] == 'type':
                    tmp = {}
                    if sent['order'][i + 1] == 'amt':
                        tmp = {'type': sent['type'][label_count['type']], 'amt': sent['amt'][label_count['amt']]}
                    elif sent['order'][i + 1] == 'actual':
                        tmp = {'type': sent['type'][label_count['type']], 'amt': sent['actual'][label_count['actual']]}
                    elif sent['order'][i + 1] == 'total':
                        tmp = {'type': sent['type'][label_count['type']], 'amt': sent['total'][label_count['total']]}
                    if tmp:
                        if 'organization/person name' in win:
                            res.append({**tmp, **win})
                        res.append({**tmp, **lose})
                label_count[sent['order'][i]] += 1
        elif len(payer) > 1:
            label_count = collections.Counter()
            for i in range(len(sent['order']) - 1):
                if sent['order'][i] == 'payer':
                    lose['organization/person name'] = sent['payer'][label_count['payer']]
                if sent['order'][i] == 'type':
                    tmp = {}
                    if sent['order'][i + 1] == 'amt':
                        tmp = {'type': sent['type'][label_count['type']], 'amt': sent['amt'][label_count['amt']]}
                    if tmp:
                        if 'organization/person name' in win:
                            res.append({**tmp, **win})
                        if 'organization/person name' in lose:
                            res.append({**tmp, **lose})
                label_count[sent['order'][i]] += 1

    return res


def litigation_cost_extraction(_sent):
    sent = copy.deepcopy(_sent)
    res = []

    base = {
        'n_doc_id': sent['文档名称'],
        'judgmentItemNo': sent['判决语句编号']
    }
    if 'fyPayer' in sent:
        if len(sent['fyPayer']) == 1:
            label_count = collections.Counter()
            for i in range(len(sent['order']) - 1):
                tmp = {}
                if sent['order'][i] == 'fyType':
                    if sent['order'][i + 1] == 'fyAmt':
                        if i < len(sent['order']) - 3 and sent['order'][i + 2] == 'fyDiscount' and sent['order'][i + 3] == 'fyActual':
                            tmp = {
                                **base,
                                'role': '承担方',
                                'organization/person name': sent['fyPayer'][0],
                                'fyAmt': sent['fyActual'][label_count['fyActual']],
                                'fyType': sent['fyType'][label_count['fyType']]
                            }

                        else:
                            tmp = {
                                **base,
                                'role': '承担方',
                                'organization/person name': sent['fyPayer'][0],
                                'fyAmt': sent['fyAmt'][label_count['fyAmt']],
                                'fyType': sent['fyType'][label_count['fyType']]
                            }
                        res.append(tmp)
                label_count[sent['order'][i]] += 1
        elif len(sent['fyPayer']) > 1:
            label_count = collections.Counter()
            for i in range(len(sent['order']) - 1):
                tmp = {}
                if sent['order'][i] == 'fyPayer':
                    if sent['order'][i + 1] == 'fyShare':
                        tmp = {
                            'role': '承担方',
                            'organization/person name': sent['fyPayer'][label_count['fyPayer']],
                            'fyShare': sent['fyShare'][label_count['fyShare']],
                            'fyType': '、'.join(sent['fyType']) if 'fyType' in sent else '',
                            **base
                        }
                        res.append(tmp)
                label_count[sent['order'][i]] += 1
    return res


def extract_relation(labels, name):
    sents = labels_to_list(labels, name)
    res = []
    for k, v in sents.items():
        res.extend(compensation_extraction(v))
        res.extend(litigation_cost_extraction(v))
    return res


if __name__ == '__main__':
    # TO DO: Add unit test
    pass