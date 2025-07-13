// Custom interactive component for UI logic

import { useState } from 'react'
import { simulateFight } from './api'

function FightSimulator() {
    const [fighter1, setFighter1] = useState('')
    const [fighter2, setFighter2] = useState('')
    const [result, setResult] = useState(null)
    const [err, setError] = useState('')


    const handleSimulate = async () => {
        try {
            const res = await simulateFight(fighter1, fighter2);
            setResult(res)
            setError('')
        } catch (err) {
            setResult(null)
            setError(err.message || 'An error has occured')
        }
    };

    return (
        <div className="fight-sim">
            <h1>UFC Fight Simulator</h1>
            <p>Ready to fight? Click "Fight" button below</p>
            <button onClick={handleSimulate}>Fight</button>
        </div>
    );
}

export default FightSimulator;