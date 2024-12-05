import React, { useState, useEffect } from 'react';

const Dashboard = () => {
    const [marketData, setMarketData] = useState({});
    const [signal, setSignal] = useState('');

    useEffect(() => {
        fetch('/api/market_data')
            .then(response => response.json())
            .then(data => {
                setMarketData(data);
            });
    }, []);

    const handleTrade = (action) => {
        fetch(`/api/trade/${action}`, {
            method: 'POST',
        });
    };

    return (
        <div>
            <h1>Forex Trading Dashboard</h1>
            <p>Market Price: {marketData.price}</p>
            <p>Trade Signal: {signal}</p>
            <button onClick={() => handleTrade('buy')}>Buy</button>
            <button onClick={() => handleTrade('sell')}>Sell</button>
        </div>
    );
};

export default Dashboard;
