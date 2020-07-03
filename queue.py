class queue:
    my_list=['3','4','5']
    def pop(self):
        if(len(self.my_list)==0):
            return 'None'
        l=self.my_list[0]
        self.my_list.remove(self.my_list[0])
        return l
    def push(self,word):
       self.my_list.append(word)
       return self.my_list

word='6'
q=queue()
first_element=q.push(word)
print(first_element)
second_element=q.pop()
print(second_element)
complete_queue=q.pop()
print(complete_queue)
third_element=q.pop()
print(third_element)
fourth_element=q.pop()
print(fourth_element)
fifth_element=q.pop()
print(fifth_element)
