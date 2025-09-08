import Avatar from '@mui/material/Avatar';
import Box from '@mui/material/Box';
import Tab from '@mui/material/Tab';
import Tabs from '@mui/material/Tabs';
import React, { useState } from 'react';

import './Navbar.css';

const Navbar: React.FC = () => {
    const [value, setValue] = useState<number>(0);
    const Tab_labels = ['View productions', 'Upload folder', 'Login', 'Home Page',];
    const Avatar_src = '/images/Generic_avatar.png';

    const handleChange = (_event: React.SyntheticEvent, newValue: number) => {
        setValue(newValue);
    };

    return (
        <Box component='nav' className='navbar-container'>
            <div className='avatar-wrapper'>
                <Avatar alt='Avatar' src={Avatar_src} />
            </div>

            <div className='navbar-tabs-wrapper'>
                <Tabs
                    className='navbar-tabs'
                    onChange={handleChange}
                    textColor='inherit'
                    value={value}
                >
                    {Tab_labels.map(label => (
                        <Tab key={label} label={label} />
                    ))}
                </Tabs>
            </div>
        </Box>
    );
};

export default Navbar;
