import React, { useEffect, useRef } from 'react';
import Plotly from 'plotly.js-dist';

const RealTimeChart = () => {
    const chartRef = useRef();

    useEffect(() => {
        const interval = setInterval(() => {
            fetch('/api/market_data')
                .then(response => response.json())
                .then(data => {
                    Plotly.react(chartRef.current, [{
                        x: data.timestamps,
                        y: data.prices,
                        type: 'scatter',
                        mode: 'lines',
                    }]);
                });
        }, 1000);
        
        return () => clearInterval(interval);
    }, []);

    return <div ref={chartRef} style={{ width: '100%', height: '500px' }} />;
};

export default RealTimeChart;
