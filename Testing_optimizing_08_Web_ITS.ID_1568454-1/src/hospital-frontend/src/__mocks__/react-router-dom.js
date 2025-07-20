import React from 'react';

const BrowserRouter = ({ children }) => <div>{children}</div>;
const Routes = ({ children }) => <>{children}</>;
const Route = ({ element }) => element;
const Link = ({ to, children, ...props }) => <a href={to} {...props}>{children}</a>;

export {
  BrowserRouter, Routes, Route, Link,
};
export default {
  BrowserRouter,
  Routes,
  Route,
  Link,
};
