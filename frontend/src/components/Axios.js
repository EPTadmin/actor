import axios from 'axios'

const baseUrl = 'http://129.241.63.74:8000/'

const AxiosInstance = axios.create({
    baseURL :baseUrl,
    timeout:5000,
    headers:{
        "Content-Type" : "application/json",
        accept : "application/json"
    }

})

export default AxiosInstance
