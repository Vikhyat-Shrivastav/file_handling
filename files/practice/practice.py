

friends=['vikhyat\n','vivek\n','tushar\n','pankaj\n','prince\n']
file=open('data.txt','w')
file.writelines(friends)
file.close()

Enemies=('chandan\n','ratan\n','rishab\n')
file=open('data.txt','a')
file.writelines(Enemies)
file.close()

friends=['manish \n']
file=open('data.txt','r')
friends=file.read()
print(friends)
file.close()