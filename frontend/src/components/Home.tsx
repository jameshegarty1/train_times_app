import React from 'react';
import { isAuthenticated } from '../utils/auth';
import ProfileList from './ProfileList';
import Navbar from './Navbar';
import { Container, AuthContainer, Button, Message } from './Home.styles';

export default function Home() {
  console.log('Home component rendered');

  return (
    <Container>
      <Navbar />
      {isAuthenticated() ? (
        <ProfileList />
      ) : (
        <AuthContainer>
          <Message>Welcome! Please log in or sign up to continue.</Message>
          <Button onClick={() => window.location.href = '/login'}>Login</Button>
          <Button onClick={() => window.location.href = '/signup'}>Sign Up</Button>
        </AuthContainer>
      )}
    </Container>
  );
};
