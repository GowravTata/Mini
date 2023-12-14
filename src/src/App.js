import { Provider } from 'react-redux';
import { createStore, applyMiddleware } from 'redux';

import { Box } from './index'

const store = createStore(() => [], {}, applyMiddleware());
function App() {
  return (
    <Provider store={store}>
      <Box />
    </Provider>
  );
}

export default App;
