# # Day 08 =Selection sort 
# input = [2,6,5,7,9,3,0]
# output = [0, 2, 3, 5, 6, 7, 9]
# time complexcity = O(n(n+1)/2)= O(n2)


def select_sort(num):
    n=len(num)
    for i in range (0,n):
        #  1 ITERRATION CHLEGA 0 SE N TK FIRST ELEMENT KO MIN_INDEX MAN LEGE OR J KA LOOP CHLYEGE 
        min_index=i
        for j in range (i+1,n):
            # J KA LOOP I+1 SE N TK CHLEGA OR AGR KOI MIN_INDEX(I)SE SMALL MILTA HAI TO US SE SWAP KRDEGA SBSE SMALL PE HI SWAP KRNA HAI OR SIRF SMALL PE TO MIN_INDEX J KO BNANA HAI 
            if num[min_index]> num[j]:
                #  CONDITION TO CHECK J MIN_INDEX SE SMALL HAI YA NHI AGR HAI TO MIN_INDEX J KO BNAO !
                min_index=j
            num[i], num[min_index]= num[min_index],num[i]
            # SWAP KRNE KI 
    return num
    

print(select_sort([2,6,5,7,9,3,0]))             







