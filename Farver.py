def print_format_table():
    """
    printer en tabel af formaterede tekst liner med farver
    """
    for style in range(8):
        for fg in range(30,38):
            s1 = ''
            for bg in range(40,48):
                format = ';'.join([str(style), str(fg), str(bg)])
                s1 += '\x1b[%sm %s \x1b[0m' % (format, format)
            print(s1)
        print('\n')

print_format_table()
print('\x1b[7;30;44m' + 'Success!' + '\x1b[0m')
