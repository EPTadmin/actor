import axios from 'axios'

const baseUrl = '/api/'

const AxiosInstance = axios.create({
    baseURL :baseUrl,
    timeout:5000,
    headers:{
        "Content-Type" : "application/json",
        accept : "application/json"
    }

})

export default AxiosInstance
