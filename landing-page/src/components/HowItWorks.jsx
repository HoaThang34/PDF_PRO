const steps = [
  { step: '1', title: 'Tải file lên', desc: 'Chọn file PDF từ máy tính hoặc kéo và thả vào công cụ' },
  { step: '2', title: 'Chỉnh sửa / Xử lý', desc: 'Sử dụng các công cụ chỉnh sửa, merge, split, compress,...' },
  { step: '3', title: 'Tải xuống kết quả', desc: 'Tải file đã xử lý về máy với chất lượng cao nhất' },
]

export default function HowItWorks() {
  return (
    <section className="how-it-works">
      <div className="container">
        <div className="section-header">
          <h2>Chỉ 3 bước đơn giản</h2>
          <p>Bắt đầu xử lý PDF của bạn chỉ với vài click chuột</p>
        </div>
        <div className="steps">
          {steps.map((s, i) => (
            <div key={i} className="step-card">
              <div className="step-num">{s.step}</div>
              <h3>{s.title}</h3>
              <p>{s.desc}</p>
              {i < steps.length - 1 && <div className="step-line" />}
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
