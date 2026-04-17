import { useState, useRef, useEffect } from "react";
import { sendMessage } from "../services/api";
import "./Chat.css"

export default function Chat() {
    const [messages, setMessages] = useState([]);
    const [input, setInput] = useState("");
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages, isLoading]);

    const handleSend = async () => {
        if (!input.trim() || isLoading) return;

        const newMessages = [...messages, { role: "user", content: input }];
        setMessages(newMessages);
        setInput("");
        setIsLoading(true);
        
        try {
            const res = await sendMessage(input);
            setMessages([
                ...newMessages,
                { role: "assistant", content: res.response }
            ]);
        } catch (error) {
            setMessages([
                ...newMessages,
                { role: "assistant", content: "El conocimiento está nublado en este momento. Intenta de nuevo." }
            ]);
        } finally {
            setIsLoading(false);
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };

    return (
        <main className="chat">
            <section className="chat__container">
                <header className="chat__header">
                    <h2 className="chat__title">AI Chat</h2>
                    <p className="chat__subtitle">Conocimiento Profundo</p>
                </header>

                <div className="chat__messages" aria-live="polite">
                    {messages.length === 0 && (
                        <div className="chat__empty-state">
                            <p>Escribe tu consulta y el abismo responderá...</p>
                        </div>
                    )}
                    {messages.map((m, i) => (
                        <div key={i} className={`chat__bubble chat__bubble--${m.role}`}>
                            <span className="chat__bubble-role">{m.role === "user" ? "Tú" : "Oráculo"}</span>
                            <div className="chat__bubble-content">{m.content}</div>
                        </div>
                    ))}
                    {isLoading && (
                        <div className="chat__bubble chat__bubble--assistant chat__bubble--loading">
                            <div className="chat__typing-indicator">
                                <span></span><span></span><span></span>
                            </div>
                        </div>
                    )}
                    <div ref={messagesEndRef} />
                </div>

                <div className="chat__input-group">
                    <input
                        className="chat__input"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyDown={handleKeyDown}
                        placeholder="Escribe tu mensaje..."
                        disabled={isLoading}
                        aria-label="Mensaje para la IA"
                    />
                    <button className="chat__button" onClick={handleSend} disabled={isLoading || !input.trim()}>
                        Enviar
                    </button>
                </div>
            </section>
        </main>
    );
}