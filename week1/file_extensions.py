name=input('File name: ').strip().casefold().split('.')
match name[-1]:
    case 'jpg' | 'jpeg':
        print('image/jpeg')
    case 'gif':
        print('image/gif')
    case 'png':
        print('image/png')
    case 'pdf':
        print('application/pdf')
    case 'txt':
        print('text/plain')
    case 'zip':
        print('application/zip')
    case _:
        print('application/octet-stream')