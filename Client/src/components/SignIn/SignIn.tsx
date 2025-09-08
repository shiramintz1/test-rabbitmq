import Button from '@mui/material/Button';
import InputAdornment from '@mui/material/InputAdornment';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';
import { useState } from 'react'

import { validateUserDetails } from './SignInValidation';
import './SignIn.css'
export const SignIn = () => {

  const Icon_src = '/images/icon.png';

  interface UserDetails {
    userName: string;
    fullName:string;
    email: string;
    password: string;
  }
  const [errors, setErrors] = useState<{ [key in keyof UserDetails]?: string }>({});
  const [users, setUsers] = useState<UserDetails[]>([]);
  const [userDetails, setUserDetails] = useState<UserDetails>(
    {
      userName: '',
      fullName:'',
      email: '',
      password: '',
    }
  )
  const handleClear = (fieldName: keyof UserDetails) => () => {
    setUserDetails((prev) => ({
      ...prev,
      [fieldName]: '',
    }));
  };
  const submit = (e) => {
    e.preventDefault();
    const validationErrors = validateUserDetails(userDetails);
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
      return;
    }
    setErrors({});
    const newUser: UserDetails = { ...userDetails };
    setUsers([...users, newUser]);
  }

  return <>
    <Stack
      component='form'
      onSubmit={submit}
      spacing={3}
      alignItems='center'
      noValidate
      autoComplete='off'
      className='sign-in-form'
    >
      <Typography variant='h4' component='h2' className='sign-in-title'>
        SignUp
      </Typography>
      <TextField
        label='User name'
        variant='filled'
        className='text-field'
        value={userDetails.userName}
        error={!!errors.userName}
        helperText={errors.userName}
        onChange={(e) => setUserDetails({ ...userDetails, userName: e.target.value })}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <img src={Icon_src} alt="icon" style={{ width: 20, height: 20 }} onClick={handleClear('password')} />
            </InputAdornment>
          ),
        }}
      />
      <TextField
        label='Full name'
        variant='filled'
        className='text-field fullName'
        value={userDetails.fullName}
        error={!!errors.fullName}
        helperText={errors.fullName}
        onChange={(e) => setUserDetails({ ...userDetails, fullName: e.target.value })}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <img src={Icon_src} alt="icon" style={{ width: 20, height: 20 }} onClick={handleClear('fullName')} />
            </InputAdornment>
          ),
        }}
      />
      <TextField
        label='Email'
        variant='filled'
        className='text-field'
        type='email'
        value={userDetails.email}
        error={!!errors.email}
        helperText={errors.email}
        onChange={(e) => setUserDetails({ ...userDetails, email: e.target.value })}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <img src={Icon_src} alt="icon" style={{ width: 20, height: 20 }} onClick={handleClear('email')} />
            </InputAdornment>
          ),
        }}
      />
      <TextField
        label='Password'
        variant='filled'
        className='text-field'
        type='password'
        value={userDetails.password}
        error={!!errors.password}
        helperText={errors.password}
        onChange={(e) => setUserDetails({ ...userDetails, password: e.target.value })}
        InputProps={{
          endAdornment: (
            <InputAdornment position="end">
              <img src={Icon_src} alt="icon" style={{ width: 20, height: 20 }} onClick={handleClear('password')} />
            </InputAdornment>
          ),
        }}
      />




      <Stack direction='row' spacing={6}>
        <Button type='submit' variant='contained' className='button register-button'>
          Register
        </Button>
        <Button variant='contained' className='button haveAccount-button'>
          Already have an account?
        </Button>
      </Stack>
    </Stack>
  </>

}