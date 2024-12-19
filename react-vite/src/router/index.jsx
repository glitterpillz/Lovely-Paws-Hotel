import { createBrowserRouter } from "react-router-dom";
import Layout from "./Layout";
import LandingPage from "../components/LandingPage";
import ServicesPage from "../components/ServicesPage";
import ReviewsPage from "../components/ReviewsPage";

export const router = createBrowserRouter([
  {
    path: "/",
    element: <LandingPage />,
  },
  {
    element: <Layout />,
    children: [
      {
        path: "services",
        element: <ServicesPage />,
      },
      {
        path: "reviews",
        element: <ReviewsPage />
      }
    ],
  },
]);
