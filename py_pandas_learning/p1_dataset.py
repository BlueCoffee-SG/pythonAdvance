
from sklearn import dataset #引入数据集
#鸢尾花数据集
iris=dataset.load_iris()
x,y=iris.data,iris.target

#查看特征
iris.feature_names

#查看标签
iris.target_names

#按照3比1的比例划分训练集与验证集
from sklearn.model_selection import train_test_split

X_train,X_test,y_tain,y_test=train_test_split(X,y,test_size=0.25)

