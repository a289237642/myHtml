/**
 * 发送异步请求，封装 axios
 **/

import axios from 'axios'

export default function ajax(url, data = {}, type = 'GET') {
    if (type === 'GET') {
        return axios.get(url, {
            params: {ID: 1234}
        })
    } else {
        return axios.post()
    }

}
