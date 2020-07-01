import pandas as pd
info="hgiesrg"

Am,F,tim,result=1,2,3,5
para_num=[3,4,5]
text="husag"
df1=pd.DataFrame([Am,F,tim,para_num[0],para_num[1],para_num[2],result,text],columns=['参数结果'],
                 index=["步幅（°）","步频（步/分）","转弯时间（s）","对称性","相关性","迟缓性","综合指标","评估结果"])
# df1 = pd.DataFrame({"步幅（°）": Am, "步频（步/分）": F,"转弯时间（s）": tim,
#                             "对称性": para_num[0], "相关性": para_num[1], "迟缓性": para_num[2],
#                             "综合指标": result, "评估结果": text
#                             })
with pd.ExcelWriter('result.xls') as writer:
    df1.to_excel(writer, sheet_name='sheet1')