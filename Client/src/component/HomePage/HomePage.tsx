import React from 'react';
import { Box, Button } from '@mui/material';
import './Home.css';

const HomePage: React.FC = () => {
  return (
    <Box className='page-container'>
    
      <Box className='main-content'>
        <img
          src='/assets/pix-stream.png'
          alt='PixStream Logo'
          className='main-image'
        />
        <Button className='login-button' variant='outlined'>
          Login
        </Button>
      </Box>
    </Box>
  );
};

export default HomePage;
