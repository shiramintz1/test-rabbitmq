import React, { useState } from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import CloseIcon from '@mui/icons-material/Close';
import Dialog from '@mui/material/Dialog';
import DialogActions from '@mui/material/DialogActions';
import DialogContent from '@mui/material/DialogContent';
import DialogTitle from '@mui/material/DialogTitle';
import IconButton from '@mui/material/IconButton';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import VisibilityIcon from '@mui/icons-material/Visibility';
import VisibilityOffIcon from '@mui/icons-material/VisibilityOff';
import { useDispatch } from 'react-redux';
import { useNavigate } from 'react-router-dom';
import { setCurrentUser } from '../../redux/slices/userSlice';

import './Login.css';
import { validateUserDetails, ValidationErrors } from './LoginValidation';

const iconSrc = '/images/icon.png';

const LABELS = {
  cancel: 'Cancel',
  closeAriaLabel: 'Close',
  forgotPassword: 'Forgot password',
  fullName: 'Full name',
  iconAlt: 'icon',
  lockIconAlt: 'lock icon',
  password: 'Password',
  signIn: 'Sign In',
};

const FORGOT_PASSWORD_MESSAGE = 'A password has been sent to your email, please enter it.';

const Login: React.FC = () => {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const [dialogOpen, setDialogOpen] = useState<boolean>(false);
  const [userName, setuserName] = useState<string>('');
  const [password, setPassword] = useState<string>('');
  const [showPassword, setShowPassword] = useState<boolean>(false);
  const [alertMessage, setAlertMessage] = useState<string>('');
  const [errors, setErrors] = useState<ValidationErrors>({});

  const resetFields = () => {
    setuserName('');
    setPassword('');
    setAlertMessage('');
    setErrors({});
    setShowPassword(false);
  };

  const handleSignIn = () => {
    const validationErrors = validateUserDetails({ userName: userName, password });
    setErrors(validationErrors);
    if (Object.keys(validationErrors).length > 0) return;

    const USERS = [
      { userName: 'user1', password: '1234', email: 'user1@example.com' },
      { userName: 'user2', password: 'abcd', email: 'user2@example.com' },
    ];
    const user = USERS.find(u => u.userName === userName);

    if (user) {
      if (user.password === password) {
        dispatch(setCurrentUser(user));
        setAlertMessage('Login successful!!!');
        navigate('/dashboard'); // navigate after successful login
      } else {
        setAlertMessage('Incorrect password, Please try again.');
      }
      setDialogOpen(true);
    } else {
      setAlertMessage('User not found, Redirecting to Sign Up...');
      setDialogOpen(true);
      setTimeout(() => navigate('/signUp'), 3000);
    }
  };

  const handleCloseDialog = () => {
    setDialogOpen(false);
    resetFields();
  };

  const handleuserNameChange = (val: string) => {
    setuserName(val);
    const validationErrors = validateUserDetails({ userName: val, password });
    setErrors(prev => ({ ...prev, userName: validationErrors.userName }));
  };

  const handlePasswordChange = (val: string) => {
    setPassword(val);
    const validationErrors = validateUserDetails({ userName: userName, password: val });
    setErrors(prev => ({ ...prev, password: validationErrors.password }));
  };

  return (
    <Box className='login-container'>
      <Box className='login-box'>
        <Typography variant='h5' align='center' color='#000000' className='login-title'>
          Login
        </Typography>
        <Box className='input-wrapper'>
          <TextField
            variant='outlined'
            label={LABELS.fullName}
            type='text'
            fullWidth
            className='input-field'
            value={userName}
            onChange={e => handleuserNameChange(e.target.value)}
            error={!!errors.userName}
            helperText={errors.userName}
          />
          <IconButton
            size='small'
            onClick={() => handleuserNameChange('')}
            className='input-icon'
          >
            <Box component='img' src={iconSrc} alt={LABELS.iconAlt} />
          </IconButton>
        </Box>

        <Box className='input-wrapper' position='relative'>
          <TextField
            variant='outlined'
            label={LABELS.password}
            type={showPassword ? 'text' : 'password'}
            fullWidth
            className='input-field'
            value={password}
            onChange={e => handlePasswordChange(e.target.value)}
            error={!!errors.password}
            helperText={errors.password}
          />
          <IconButton
            size='small'
            onClick={() => handlePasswordChange('')}
            style={{ position: 'absolute', right: 10, top: 10 }}
          >
            <Box component='img' src={iconSrc} alt={LABELS.lockIconAlt} />
          </IconButton>
          <IconButton
            size='small'
            onClick={() => setShowPassword(prev => !prev)}
            style={{ position: 'absolute', right: 40, top: 10 }}
          >
            {showPassword ? <VisibilityOffIcon /> : <VisibilityIcon />}
          </IconButton>
        </Box>

        <Box className='buttons-row'>
          <Button variant='contained' className='signin-button' onClick={handleSignIn}>
            {LABELS.signIn}
          </Button>
          <Button
            variant='contained'
            className='forgot-button'
            onClick={() => {
              setAlertMessage(FORGOT_PASSWORD_MESSAGE);
              setDialogOpen(true);
            }}
          >
            {LABELS.forgotPassword}
          </Button>
        </Box>
      </Box>

      <Dialog open={dialogOpen} onClose={handleCloseDialog} className='custom-dialog'>
        <DialogTitle className='dialog-title'>
          {alertMessage === FORGOT_PASSWORD_MESSAGE ? 'Enter mail' : 'Notification'}
          <IconButton aria-label={LABELS.closeAriaLabel} onClick={handleCloseDialog} className='dialog-close-button'>
            <CloseIcon />
          </IconButton>
        </DialogTitle>
        <DialogContent className='dialog-content'>
          <Typography className='dialog-text'>{alertMessage}</Typography>
        </DialogContent>
        <DialogActions className='dialog-actions'>
          <Button onClick={handleCloseDialog} className='cancel-button'>{LABELS.cancel}</Button>
        </DialogActions>
      </Dialog>
    </Box>
  );
};

export default Login;
