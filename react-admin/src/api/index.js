/**n个接口请求函数的模块**/
import ajax from './ajax'

// const BASE="http://127.0.0.1:5000"
const BASE = ''
//login
export const reqLogin = (username, password) => ajax(BASE + '/login', {username, password}, "POST")
//add user
export const reqAddUser = (user) => ajax(BASE + '/manage/user/add', user, "POST")
