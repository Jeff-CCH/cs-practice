"""
When Bob wants to send Alice a message M on the Internet, he breaks M into n data packets, numbers the packets consecutively, and injects them into the network. When the packets arrive at Alice's computer, they may be out of order, so Alice must assemble the sequence of n packets in order before she can be sure she has the entire message. Describe an efficient scheme for Alice to do this, assuming that she knows the value of n. What is the running time of this algorithm?
"""

# merge sort, cost O(nlogn)
def merge_sort(msg):
    if len(msg) == 1:
        return msg
    else:
        result = []
        half_len = len(msg) // 2
        left_msg = msg[half_len:]
        right_msg = msg[:half_len]
        res_left = merge_sort(left_msg)
        res_right = merge_sort(right_msg)
        
        i=j=0
        while i < len(res_left) or j < len(res_right):
            if i < len(res_left) and j < len(res_right):
                if res_left[i][0] < res_right[j][0]:
                    result.append(res_left[i])
                    i += 1
                else:
                    result.append(res_right[j])
                    j += 1
            elif i < len(res_left):
                result.append(res_left[i])
                i += 1
            else: # j < len(right_msg):
                result.append(res_right[j])
                j += 1

        return result        

def rcv_msg(msg):
    ordered_msg = merge_sort(msg)
    for m in ordered_msg:
        print m

def main():
    bob_msg = [(0, 'Hi'), (2,'Nice to meet u'), (4,':))'), (1,'I am Bob'), (3,'.')]
    rcv_msg(bob_msg)

if __name__ == '__main__':
    main()
