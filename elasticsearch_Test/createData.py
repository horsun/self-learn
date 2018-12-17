
import random

from mongoTest.MongoClient_TEST import MongoClient

listFirstName = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '张', '李', '金']
listSecondName = ['豫', '章', '故', '郡', '洪', '都', '新', '府', '星', '分', '翼', '轸', '地', '接', '衡', '庐', '襟', '三', '江', '而',
                  '带', '五', '湖', '控', '蛮', '荆', '而', '引', '瓯', '越', '物', '华', '天', '宝', '龙', '光', '射', '牛', '斗', '之',
                  '墟', '人', '杰', '地', '灵', '徐', '孺', '饯', '子']
listAge = [18, 19, 20, 21, 22, 23, 24]
listSex = ['male', 'female']


def createRandomPerson():
    person = {}
    rName = random.choice(listFirstName) + random.choice(listSecondName)
    person['name'] = rName
    person['age'] = random.choice(listAge)
    person['sex'] = random.choice(listSex)
    return person


for i in range(100):
    MongoClient().create_collection(db_name='esDb', coll_name='userInfo').insert(
        createRandomPerson()
    )
