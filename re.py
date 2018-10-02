##import re
##count=0
##pattern=re.compile('python')
##print(type(pattern)) 
##matcher=pattern.finditer("learning python is very easy python hi..love you python")
##for match in matcher:
##    count+=1
##    print("Match found at:", match.start())
##    print("End found at:", match.end())
##    print("Group found at:", match.group())
##print("The number of ocurrences: ",count)
##
##count=0
##matcher=re.finditer('abc','abcdabcfabchabchabck')
##for i in matcher:
##    print(i.start())
import re
matcher=re.findall('python','python is nice python python hiojdioghdsfgkjh python')
print(matcher)
