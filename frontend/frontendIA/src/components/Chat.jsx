import { useState } from "react";
import { sendMessage } from "../services/api";
import "./Chat.css"

export default function Chat(){
    const [messages, setMessages]= useState([])
    const [input,setInput]= useState("")



    const handleSend = async () =>{
        if(!input) return;

        const newMessages=[...messages, {role:"user",content:input}]
        setMessages(newMessages)
        
        const res= await sendMessage(input)

        setMessages([
            ...newMessages,
            {role:"assistant", content:res.response}
        ])

        setInput("")
    }
    return(

        <div className="container">

            <h2 className="container__title">AI Chat</h2>

            <div className="container__messages">

                {messages.map((m,i)=>(
                    <div key={i}>
                        <b>{m.role==="user" ? "You" : "AI"}:</b> {m.content}
                    </div>
                ))}

            </div>

            <input
                className="container__input"
                value={input}
                onChange={(e)=>setInput(e.target.value)}
            />

            <button className="container__button" onClick={handleSend}>
                Send
            </button>

        </div>
    )
}