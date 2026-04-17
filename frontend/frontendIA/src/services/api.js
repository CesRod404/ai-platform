//Post the message in the llm
export async function sendMessage(message){
    // Usa VITE_API_URL en producción (Vercel) o localhost en desarrollo
    const API_URL = import.meta.env.VITE_API_URL || "http://127.0.0.1:8000";

    const response = await fetch(`${API_URL}/chat`,{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            message:message
        })
    })

    return response.json()
}