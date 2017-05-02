"""
Write a set of Python classes that can simulate an Internet application in which one party, Alice, is periodically creating a set of packets that she wants to send to Bob. An Internet process is continually checking if Alice has any packets to send, and if so, it delivers them to Bob's computer, and Bob is periodically checking if his computer has a packet from Alice, and, if so, he reads and deletes it.
"""

class App:
    def read_msg(self, conn):
        for msg in conn:
            print msg
            conn.remove(msg)
    def send_msg(self, conn, msg):
        conn.append(msg)


def main():
    alice = App()
    bob = App()
    conn = []
    while True:
        msg = input("Please input the msg: ")
        alice.send_msg(conn, msg)
        bob.read_msg(conn)
        con = input("Continue? [y/n]: ")
        if con != 'y':
            break

if __name__ == '__main__':
    main()
