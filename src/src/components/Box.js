import { Button } from '@mui/material';
import { useDispatch, useSelector } from "react-redux";
import { TextField } from '@mui/material';
import React from 'react';
import initialState from './initialState';

import HomePageAction from '../actions/HomePageAction';

const Box = () => {
    const dispatch = useDispatch()
    const newVisible = initialState.homePage.visible
    console.log(newVisible, 'from top')
    const [visible, setVisible] = React.useState(false)
    const [signUp, setSignUp] = React.useState(false)
    return (
        <div>
            <p>
                <Button variant="text" onClick={() => {
                    HomePageAction.setAddVisible(true, dispatch)
                    setVisible(true);
                    setSignUp(false)
                }}>Login</Button>
                <Button variant="text" onClick={() => {
                    setSignUp(true);
                    setVisible(false);
                }}>Sign Up</Button>
                {
                    console.log(newVisible, 'new Visible on click') &&
                    newVisible &&

                    <div>
                        <TextField id='stabdard-basic' label='username/email' variant='standard' />
                        <TextField id='stabdard-basic' label='password' variant='standard' />
                        <Button variant="text" onClick={() => { HomePageAction.setAddVisible(false, dispatch) }}>Close</Button>
                    </div>

                }
                {
                    signUp &&
                    <div>
                        <TextField id='stabdard-basic' label='username' variant='standard' />
                        <TextField id='stabdard-basic' label='email' variant='standard' />
                        <TextField id='stabdard-basic' label='password' variant='standard' />
                        <TextField id='stabdard-basic' label='DOB' variant='standard' />
                        <Button variant="text" onClick={() => { setSignUp(false) }}>Submit</Button>
                    </div>

                }
            </p>
        </div>
    )
}

export default Box