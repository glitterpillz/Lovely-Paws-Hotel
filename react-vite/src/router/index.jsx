import { createBrowserRouter } from "react-router-dom";
import Layout from "./Layout";
import LandingPage from "../components/LandingPage";
import ServicesPage from "../components/ServicesPage";
import ReviewsPage from "../components/ReviewsPage";
import PetList from "../components/Pets/PetList";
import PetDetail from "../components/Pets/PetDetail";
import BookingCreatePage from "../components/BookingCreatePage";

const router = createBrowserRouter([
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
        element: <ReviewsPage />,
      },
      {
        path: "pets",
        element: <PetList />,
        children: [
          {
            path: ":petId",
            element: <PetDetail />,
          },
        ],
      },
      {
        path: "staff/pets",
        element: <PetList />,
        children: [
          {
            path: ":petId",
            element: <PetDetail />,
          },
        ],
      },
      {
        path: "bookings/pet/:petId",
        element: <BookingCreatePage />
      }
    ],
  },
]);

export { router };