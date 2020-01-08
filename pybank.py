import csv, os


with open('Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv') as csvfile:
    read_csv=csv.reader(csvfile, delimiter=',')
    
    
    next(read_csv)
    col_sum=[]
    row_count=[]
    average=[]
    for row in read_csv:
        row_count.append(row[0])
        col_sum.append(int(row[1]))
        
    row_count1=len(row_count)
    pl_sum=sum(col_sum)
    
    for i in range(len(col_sum)-1):
        average.append(col_sum[i+1]-col_sum[i])
        
        average_change=sum(average)/row_count1
        
        max_change=max(average)
        
        max_index=average.index(max_change)+1
        
        minus_change=min(average)
        minus_index=average.index(minus_change)+1
        
print("Financial Analysis")
print("----------------------------")
print "Total Months:",(row_count1)
print "Total: $",(pl_sum)

print "Average  Change: $",(average_change)

print "Greatest Increase in Profits:",row_count[max_index],"($",(max_change),")"


print "Greatest Decrease in Profits:",row_count[minus_index],"($",(minus_change),")"


