import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, fileName) {
  return Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]).then((results) =>
    results.map((res) => {
      if (res.status === 'fulfilled') {
        return res;
      }
      // Pour les promesses rejetées, mettre l'erreur dans 'value'
      return { status: 'rejected', value: res.reason };
    })
  );
}
