import { useState } from 'react'

function Home() {
    const [cnt, setCnt] = useState(0)
    
    useEffect(()=>{
        setCnt(cnt+1)
    },cnt)

    return (
        <div>
            <h2>환영합니다~!</h2>
        </div>
    )
}

export default Home