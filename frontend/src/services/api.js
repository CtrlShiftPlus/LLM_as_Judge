import axios from "axios";


const API = axios.create({

    baseURL:"http://127.0.0.1:8000/api",

});


export const evaluateResponse = async(data)=>{

    const response = await API.post(
        "/evaluate/",
        data
    );

    return response.data;

};