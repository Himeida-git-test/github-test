import { useState } from "react";

const MyButton = () => {
    const [count, setCount] = useState(0);

    return (
        <>
            <div>{count}</div>
            <button onClick={() => setCount((count) => count + 1)}>"테스트"</button>
        </>
    )
}
export default MyButton;