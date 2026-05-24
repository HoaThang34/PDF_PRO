import Header from './components/Header.jsx'
import Hero from './components/Hero.jsx'
import ToolsGrid from './components/ToolsGrid.jsx'
import Features from './components/Features.jsx'
import DemoSection from './components/DemoSection.jsx'
import HowItWorks from './components/HowItWorks.jsx'
import AdvancedFeatures from './components/AdvancedFeatures.jsx'
import SecuritySection from './components/SecuritySection.jsx'
import PerformanceStats from './components/PerformanceStats.jsx'
import Testimonials from './components/Testimonials.jsx'
import FAQ from './components/FAQ.jsx'
import FinalCTA from './components/FinalCTA.jsx'
import Footer from './components/Footer.jsx'
import './App.css'

export default function App() {
  return (
    <>
      <Header />
      <main>
        <Hero />
        <ToolsGrid />
        <Features />
        <DemoSection />
        <HowItWorks />
        <AdvancedFeatures />
        <SecuritySection />
        <PerformanceStats />
        <Testimonials />
        <FAQ />
        <FinalCTA />
      </main>
      <Footer />
    </>
  )
}
