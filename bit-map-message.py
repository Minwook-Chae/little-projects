import sys

bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................
"""


def main(): 
    print("bitmap message")
    print("Enter message for bitmap:")
    message = input('> ')
    if message == '':
        sys.ext()
    for line in bitmap.splitlines():
        for i, bit in enumerate(line):
            if bit == ' ':
                print(' ', end='')
            else:
                print(message[i % len(message)], end='')
        print()


if __name__ == '__main__':
    main()

