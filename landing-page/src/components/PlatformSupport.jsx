const platforms = [
  { name: 'Windows', icon: '🪟' },
  { name: 'macOS', icon: '🍎' },
  { name: 'Linux', icon: '🐧' },
  { name: 'Android', icon: '📱' },
  { name: 'iOS', icon: '📲' },
  { name: 'Web App', icon: '🌐' },
]

export default function PlatformSupport() {
  return (
    <section className="platform-support">
      <div className="container">
        <div className="section-header">
          <h2>Hỗ trợ đa nền tảng</h2>
          <p>Sử dụng PDF PRO trên mọi thiết bị và hệ điều hành</p>
        </div>
        <div className="platform-grid">
          {platforms.map((p) => (
            <div key={p.name} className="platform-card">
              <span className="platform-icon">{p.icon}</span>
              <span className="platform-name">{p.name}</span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
