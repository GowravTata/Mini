import React from 'react';
import ReactDOM from 'react-dom/client';
import configureStore from './store/configureStore';
import App from './App';

const store = configureStore()
const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

