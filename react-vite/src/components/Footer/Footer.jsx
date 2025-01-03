import { FaLinkedin, FaGithub } from "react-icons/fa";
import foot from "./Footer.module.css";

function Footer() {
  return (
    <div className={foot.mainContainer}>
      <a
        className={foot.linkButtonContainer}
        href="https://www.google.com"
        target="_blank"
        rel="noopener noreferrer"
      >
        <button className={foot.linkedin}>
          <FaLinkedin size={30} />
        </button>
      </a>
      <a
        className={foot.linkButtonContainer}
        href="https://www.google.com"
        target="_blank"
        rel="noopener noreferrer"
      >
        <button className={foot.github}>
          <FaGithub size={30} />
        </button>
      </a>
    </div>
  );
}

export default Footer;