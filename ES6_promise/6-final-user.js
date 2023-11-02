import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return new Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)])
  .then(([userResult, photoResult]) => {
    return [
      {
        firstName,
        lastName,
        ...userResult,
        photo: photoResult,
      },
    ];
  }).catch(err => err);
}
