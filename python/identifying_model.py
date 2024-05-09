import numpy as np
import sklearn.neighbors as sn
import matplotlib.pyplot as mp
from sklearn.datasets import load_digits
import sklearn.model_selection as sm2
import sklearn.metrics as sm1
import pickle
x = load_digits().data
y = load_digits().target
pics = load_digits().images

# 划分数据集
x_train, x_test, y_train, y_test = sm2.train_test_split(
    x, y, test_size=0.2, random_state=7)

# 训练模型
model = sn.KNeighborsClassifier(n_neighbors=1, leaf_size=30)
model.fit(x_train, y_train)
pred_test_y = model.predict(x_test)

# 输出分类报告
cr = sm1.classification_report(y_test, pred_test_y)
print(cr)

# 验证曲线
train_scores, test_scores = sm2.validation_curve(model, x_train, y_train, param_name="n_neighbors",
                                                 param_range=np.arange(1, 11, 1), cv=5)
mp.grid(linestyle=":")
mp.plot(np.arange(1, 11, 1), test_scores.mean(axis=1),
        "o-", color="green", label='validation curve')
mp.legend()
mp.show()

# 学习曲线
_, train_scores2, test_scores2 = sm2.learning_curve(model, x_train, y_train,
                                                    train_sizes=np.arange(0.1, 1.0, 0.1), cv=5)
mp.grid(linestyle=':')
mp.plot(np.arange(0.1, 1.0, 0.1), test_scores2.mean(axis=1),
        "o-", color="red", label='learning curve')
mp.show()

# 存储模型
with open("C:/Users/fer20/Desktop/project1/identify.pkl", 'wb') as f:
    pickle.dump(model, f)
    print("dump succeed")
