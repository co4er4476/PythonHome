#이대선--salary_output

def output(employee) :
    print("==============================================================")
    print("사번\t급수\t호\t수당\t지급액\t세금\t차인지급액")
    print("--------------------------------------------------------------")
    print(f"{employee['num']}\t{employee['geup']}\t{employee['ho']}\t{employee['sudang']:,}\t{employee['jigeup']:,}\t{employee['mytax']}\t{employee['diffamount']:,}", end='\t')