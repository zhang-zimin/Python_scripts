import requests
import time

url_login = 'http://ids.hhu.edu.cn/amserver/UI/Login'
url_submit = 'http://form.hhu.edu.cn/pdc/formDesignApi/dataFormSave?wid=A3359E1B43376F77E0538101600A8722&userId={}'
headers ={
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72'
}

local_time = time.strftime('%Y/%m/%d',time.localtime())

dic_info = {
    '万晨':{
        'login':{
        'IDToken1': '191308010004',#学号
        'IDToken2': 'passport',#密码
        'IDButton': 'Submit'

    },
    'submit':{
            'DATETIME_CYCLE': local_time,
            'XGH_566872': '191308010004',
            'XM_140773': '万晨',
            'SFZJH_402404': '321284199612066014',
            'SZDW_439708': '力学与材料学院',
            'ZY_878153': '一般力学与力学基础',
            'GDXW_926421': '硕士生',
            'DSNAME_606453': '江守燕',
            'PYLB_253720': '非定向',
            'SELECT_172548': '江宁校区01舍',
            'TEXT_91454': '220',
            'TEXT_24613': '15195965385',
            'TEXT_826040': '15195965385',
            'RADIO_479243': '否',
            'RADIO_813412': '否',
            'RADIO_49955': '健康',
            'RADIO_17769': '是',
            'RADIO_165012': '是',
            'PICKER_449470': '江苏省,南京市,江宁区'

}
    }
}



def login_func(url_login,headers,dic_login,user_name):
    response_login = requests.post(url_login,headers = headers,data = dic_login)

    # print("Status code of login:",response_login.status_code)

    # print(response_login.text)

    if '用户名或密码错误' in response_login.text:
        print('{}用户名或密码错误！'.format(user_name))
        return 1

    if response_login.status_code != 200:
        print('服务器异常！')
        return 1
    


def submit_func(url_submit,headers,dic_submit):
    response_submit = requests.post(url_submit,headers = headers,data = dic_submit)

    # print("Status of submit code:",response_submit.status_code)
    # print(response_submit.text)

    if 'true' in response_submit.text:
        # print('打卡成功!')
        return 0
    else:
        # print('打卡失败！')
        return 1

i_count = 1
for content in dic_info:
    while 1:
        a = login_func(url_login,headers,dic_info[content]['login'],content)
        b = submit_func(url_submit.format(dic_info[content]['login']['IDToken1']),headers,dic_info[content]['submit'])
        if b:
            print('{}打卡失败！{}'.format(content,str(i_count)+'/'+str(len(dic_info))))
            continue
        else:
            print('{}打卡成功!{}'.format(content,str(i_count)+'/'+str(len(dic_info))))
            break
    i_count +=1
