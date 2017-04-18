import sys,os,re

sample_data = """>Rosalind_6404
CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
TCCCACTAATAATTCTGAGG
>Rosalind_5959
CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808
CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
TGGGAACCTGCGGGCAGTAGGTGGAAT"""
counter_C1=0
counter_G1=0
counter_C2=0
counter_G2=0

text=sample_data.split("\n")
for x  in range(0,len(text)-1):
    if 'Rosalind' in text[x]:
        print ("index value is " + str(x))
        value1=text[x+1]
        len1=len(value1)
        print (len1)
        for i in range(0,len1):
            #print (value1[i])
            if 'C' in value1[i]:
                counter_C1=counter_C1+1
            if 'G' in value1[i]:
                counter_G1=counter_G1+1
        print (counter_C1)
        print (counter_G1)
        value2=text[x+2]
        len2=len(value2)
        print (len2)
        for j in range(0,len2-1):
            if 'C' in value2[j]:
                counter_C2=counter_C2+1              
            if 'G' in value2[j]:
                counter_G2=counter_G2+1
        print (counter_C2)
        print (counter_G2)
        gc_value=(counter_C1+counter_C2+counter_G1+counter_G2)/(len1+len2)
        print (gc_value*100)
        counter_C1=0
        counter_G1=0
        counter_C2=0
        counter_G2=0
        len1=0
        len2=0
print (text)
