import dotenvSafe from 'dotenv-safe';
dotenvSafe.config({
  allowEmptyValues: true,
});

export const firebase = {
  apiKey: process.env.FIREBASE_API_KEY,
  authDomain: process.env.FIREBASE_AUTH_DOMAIN,
  databaseURL: process.env.FIREBASE_DATABASE_URL,
  // storageBucket: process.env.FIREBASE_STORAGE_BUCKET,
}

export const RPi = {
  id: process.env.RPI_ID,
  key: process.env.PRI_SECRET_KEY,
}
