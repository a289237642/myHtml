/**n个接口请求函数的模块**/
import ajax from './ajax'
import jsonp from 'jsonp'

// const BASE="http://127.0.0.1:5000"
const BASE = ''
//login
export const reqLogin = (username, password) => ajax(BASE + '/login', {username, password}, "POST")
//add user
export const reqAddUser = (user) => ajax(BASE + '/manage/user/add', user, "POST")

//天气
export function reqWeather(city) {
    const url =
        `http://api.map.baidu.com/telematics/v3/weather?location=${city}&output=json&ak=3p4
9MVra6urFRGOT9s8UBWr2`
    return new Promise((resolve, reject) => {
        jsonp(url, {
            param: 'callback'
        }, (error, response) => {
            if (!error && response.status === 'success') {
                const {dayPictureUrl, weather} = response.results[0].weather_data[0]
                resolve({dayPictureUrl, weather})
            } else {
                alert('获取天气信息失败')
            }
        })
    })
}
