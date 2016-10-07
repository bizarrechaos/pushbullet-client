def device_output(jsondoc, all):
    if 'devices' in jsondoc:
        fields = ['NICKNAME',
                  'IDEN',
                  'KIND',
                  'MANUFACTURER',
                  'MODEL',
                  'PUSHABLE']
        print '{0:20} {1:30} {2:20} {3:20} {4:20} {5}'.format(*fields)
        devices = jsondoc['devices']
        if not all:
            devices = [d for d in devices if d['active']]
        for d in devices:
            for f in fields:
                if f.lower() not in d.keys():
                    d[f.lower()] = None
            print '{nickname:20} {iden:30} {kind:20} {manufacturer:20} '\
                  '{model:20} {pushable}'.format(**d)


def push_output(jsondoc, unread):
    if 'pushes' in jsondoc:
        fields = ['TYPE',
                  'IDEN',
                  'CREATED',
                  'DIRECTION',
                  'SENDER_NAME',
                  'TITLE',
                  'BODY']
        pushes = jsondoc['pushes']
        if unread:
            pushes = [p for p in pushes if not p['dismissed']]
        for p in pushes:
            for f in fields:
                if f.lower() not in p.keys():
                    p[f.lower()] = None
            print '{type:5} {iden:5} {created:5} {direction:5} '\
                  '{sender_name}\n{title}\n{body}\n'.format(**p)


def pushed_output(jsondoc):
    if jsondoc:
        print 'push sent'
    else:
        print 'push failed'
